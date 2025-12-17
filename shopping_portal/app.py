from flask import Flask, request, render_template, redirect, url_for, make_response, flash
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies

app = Flask(__name__)

# DB connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pruthvi@sql28'
app.config['MYSQL_DB'] = 'shop_db'

app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

app.secret_key = 'random_secret_string'

mysql = MySQL(app)
jwt = JWTManager(app)

#Routes

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, username FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Convert string for JWT
            access_token = create_access_token(identity=str(user[0]))
            
            resp = make_response(redirect(url_for('portal')))
            set_access_cookies(resp, access_token)
            return resp
        else:
            flash("Invalid Username or Password", "error")
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            flash("Registration Successful! Please Login.", "success")
            return redirect(url_for('login'))
        except:
            flash("Username already exists.", "error")
        finally:
            cursor.close()
            
    return render_template('register.html')

@app.route('/portal')
@jwt_required()
def portal():
    current_user_id = get_jwt_identity()
    search_query = request.args.get('q', '') # Get search term
    
    cursor = mysql.connection.cursor()
    
    # Get Username
    cursor.execute("SELECT username FROM users WHERE id = %s", (current_user_id,))
    username = cursor.fetchone()[0]

    # Fetch images
    if search_query:
        query_string = "%" + search_query + "%"
        cursor.execute("SELECT * FROM products WHERE name LIKE %s", (query_string,))
    else:
        cursor.execute("SELECT * FROM products")
    
    
    products = [{"id": p[0], "name": p[1], "price": p[2], "image": p[3]} for p in cursor.fetchall()]
    cursor.close()
    
    return render_template('portal.html', user=username, products=products)
@app.route('/cart')
@jwt_required()
def cart():
    current_user_id = get_jwt_identity()
    cursor = mysql.connection.cursor()
    
    # Get Username
    cursor.execute("SELECT username FROM users WHERE id = %s", (current_user_id,))
    username = cursor.fetchone()[0]


    cursor.execute("""
        SELECT o.id, p.name, p.price, o.order_date 
        FROM orders o 
        JOIN products p ON o.product_id = p.id 
        WHERE o.user_id = %s 
        ORDER BY o.order_date DESC
    """, (current_user_id,))
    
    orders = cursor.fetchall()
    
    # cart sum
    total_spent = sum([order[2] for order in orders]) 
    
    cursor.close()
    return render_template('cart.html', user=username, orders=orders, total=total_spent)

@app.route('/buy/<int:product_id>', methods=['POST'])
@jwt_required()
def buy_product(product_id):
    current_user_id = get_jwt_identity()
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO orders (user_id, product_id) VALUES (%s, %s)", (current_user_id, product_id))
    mysql.connection.commit()
    cursor.close()
    
    flash("Added to Cart successfully!", "success")
    return redirect(url_for('portal'))

# Remove product
@app.route('/remove_item/<int:order_id>', methods=['POST'])
@jwt_required()
def remove_item(order_id):
    current_user_id = get_jwt_identity()
    cursor = mysql.connection.cursor()
    
    # Delete the order
    cursor.execute("DELETE FROM orders WHERE id = %s AND user_id = %s", (order_id, current_user_id))
    mysql.connection.commit()
    cursor.close()
    
    flash("Item removed from cart.", "success")
    return redirect(url_for('cart'))

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    return resp

if __name__ == '__main__':
    app.run(debug=True)