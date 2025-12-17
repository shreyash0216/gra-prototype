from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "message": "GRA Prototype API is running on Vercel! 🚀",
            "status": "healthy",
            "version": "1.0.0"
        }
        
        self.wfile.write(json.dumps(response).encode())
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            
            response = {
                "message": "Query processed successfully",
                "query": data.get("query", ""),
                "response": "This is a simplified response from Vercel serverless function. Your GRA prototype is working!",
                "context": [
                    {"content": "Sample context about RAG systems", "metadata": {"source": "vercel"}},
                    {"content": "Sample context about AI simulation", "metadata": {"source": "vercel"}}
                ]
            }
        except:
            response = {"error": "Invalid JSON data"}
        
        self.wfile.write(json.dumps(response).encode())
        return