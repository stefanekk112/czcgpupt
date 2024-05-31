from flask import Flask, render_template, jsonify
from czcParser import Parser

app = Flask(__name__)
parser = Parser()

@app.route('/product-info/<product_id>')
def product_info(product_id):
    try:
        data_json = parser.parse_product(product_id)
        if data_json:
            return jsonify(data_json)
        else:
            return "No data available for this product."
    except Exception as e:
        error_msg = "An error occurred: " + str(e)
        return error_msg

if __name__ == '__main__':
    app.run(debug=True)
