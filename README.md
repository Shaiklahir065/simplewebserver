# EX01 Developing a Simple Webserver
## Date: 1/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
<html>
<head> <title>List of protocols in TCP/IP protoco suite</title>
</head
<Body>
<table align="center" border="1" bgcolour="cyan" cellpadding="10">
<caption> List of protocols in TCP/IP protoco suite</caption>
<tr><th>s.no</th><th>Name of layer</th><th>Name of Protocols</th></tr>
<tr><th>1</th><th>Application Layer</th><th>HTTP,FTP,DNS,TELNET&SSH</th></tr>
<tr><th>2</th><th>Transport Layer</th><th>TCP/UDP</th>></tr>
<tr><th>3</th><th>Network Layer</th><th>IPV4/IPV6</th></tr>
<tr><th>4</th><th>Link Layer</th><th>ETHER NET</th></tr>
</table>
</Body>
</html>
```
## OUTPUT:

![alt text](image.png)

## RESULT:
The program for implementing simple webserver is executed successfully.
