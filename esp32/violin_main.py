from machine import Pin, UART
import time
import network
import esp
import gc

try:
    import usocket as socket
except:
    import socket

esp.osdebug(None)
gc.collect()

# MODIFY PASSWORD AND SETTINGS
ssid = "TP-Link_65BE"
password = '44097783'
station = network.WLAN(network.STA_IF)

# By default, ap mode instead of sta mode. Change this.
station.active(True)
# Connect to WiFi network with above credentials
station.connect(ssid, password)

# Warning; test that credentials must be correct. Else boot.py stuck here
while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)

def web_page():
    if curr_time == '':
        gpio_state="OFF"
    else:
        gpio_state= curr_time

    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
    <p>Current Time: <strong>""" + gpio_state + """</strong></p><p><a href="/?music=on"><button class="button">Music</button></a></p>
    </body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Updates from OpenMV send
curr_time = ''

# uart init
uart= UART(2,115200)
uart.init(115200,bits=8, parity=None, stop=1)

while True:
    conn, addr = s.accept()
    time.sleep(0.1)
    # Update based on uart read
    read = uart.readline()
    if read == None:
        pass
    # At least do a type check for URL error
    else:
        curr_time = read.decode("ascii")
        curr_time = curr_time.rstrip()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    music_on = request.find('/?music=on')
    if music_on == 6:
        print('Music Redirecting!')
        # Send the redirect request to youtube
        conn.send('HTTP/1.1 302 Found\n')
        if curr_time == '':
            conn.send('Location: https://www.youtube.com/watch?v=ZIBT-vBHgJc' + curr_time)
        else:
            conn.send('Location: https://www.youtube.com/watch?v=ZIBT-vBHgJc&feature=youtu.be&t=' + curr_time)
            print('Arriving at: ' + curr_time)
        conn.close()
        continue
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')

    conn.sendall(response)
    conn.close()

