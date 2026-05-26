from flask import Flask, jsonify                                                                                                                                                                        
import os                                                                                                                                                                                             
                                                                                                                                                                                                          
app = Flask(__name__)
                                                                                                                                                                                                          
@app.route('/api/health')                                                                                                                                                                             
def health():
    return jsonify({"status": "ok"})