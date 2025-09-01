from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head> <title>my first page</title>
</head
<Body>
<table align="center" border="1" bgcolour="cyan" cellpadding="10">
<caption>LIST OF PROTOCOLS IN TCP/IP PROTOCOL SUITE</caption>
<tr><th>s.no</th><th>Name of th Layer</th><th>Name of the protocol</th></tr>
<tr><th>1</th><th>Application Layer</th><th>HTTPS,FTP,DNS,TELNET ANS SSH</th></tr>
<tr><th>2</th><th>Transport Layer</th><th>TCP/UDP</th></tr>
<tr><th>3</th><th>Network Layer</th><th>IPV4/IPV6</th></tr>
<tr><th>4</th><th>Link Layer</th><th>Ethernet</th></tr>
</table>
</Body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()