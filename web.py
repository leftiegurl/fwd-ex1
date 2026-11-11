from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocols</title>
</head>

<body>

    <h1>TCP/IP Protocols</h1>
    <hr>

    <h2>Introduction</h2>
    <p>
        TCP/IP is a set of communication protocols used
        to connect devices over the Internet.
    </p>

    <h2>Types of Protocols</h2>

    <h3>1. Application Layer</h3>
    <ul>
        <li>HTTP - Used for web browsing.</li>
        <li>HTTPS - Provides secure web communication.</li>
        <li>FTP - Transfers files.</li>
        <li>DNS - Converts domain names into IP addresses.</li>
        <li>SMTP - Used for sending emails.</li>
    </ul>

    <h3>2. Transport Layer</h3>
    <ul>
        <li>TCP - Provides reliable data transmission.</li>
        <li>UDP - Provides faster data transmission.</li>
    </ul>

    <h3>3. Internet Layer</h3>
    <ul>
        <li>IP - Handles addressing and routing.</li>
        <li>ICMP - Reports network errors.</li>
        <li>IGMP - Manages multicast communication.</li>
    </ul>

    <h3>4. Network Access Layer</h3>
    <ul>
        <li>Ethernet - Supports wired communication.</li>
        <li>Wi-Fi - Supports wireless communication.</li>
        <li>PPP - Establishes point-to-point connections.</li>
    </ul>

    <h2>Conclusion</h2>
    <p>
        TCP/IP protocols enable reliable communication
        and data exchange between devices across networks.
    </p>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',680)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()