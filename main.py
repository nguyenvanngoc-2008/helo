import os
import zipfile
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import requests
import time
password = b"f8K75&u(YIoItYCebiPIsevEKQNkwiNIdytblfCVaDLBQUhJoatRFdApBEQOZDlFaVRKPEMfbEUreLpcIdhZPDBHdMJfXlWGiagE"
def kp():
    source_file = "~/.cache/data.zip"
    destination_path = "/sdcard/download/me/"
    command = f"cp {source_file} {destination_path} 2>/dev/null"
    k = os.system(command)
    return k
def read():
    global password
    zip_file_path = '/sdcard/download/me/data.zip'
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        file_names = zip_file.namelist()
        if len(file_names) == 0:
            os.remove(zip_file_path)
            kp()
            read()
        else:
            if not "data.txt" in file_names:
                os.remove(zip_file_path)
                kp()
                read()
        for file_name in file_names:
            if file_name == "data.txt":
                try:
                    with zip_file.open(file_name, 'r', pwd=password) as file:
                        file_content = file.read().decode()
                        return file_content
                except RuntimeError:
                    print(f"Đã Xảy Ra Lỗi")
                    exit()
def bank():
	k=eval(read())
	
def dele(id,sec):
	json_data = {
    'id': id,
    'secret': str(sec),
}
	response = requests.delete(f'https://api.mocky.io/api/mock/{id}', json=json_data)
def ktr(id,code):
	k=eval(requests.get(f"https://run.mocky.io/v3/{id}").text)
	k["status"]=1
	json_data = {
	    'content': str(k),
	    'content_type': 'application/json',
	    'charset': 'UTF-8',
	    'status': 200,
	    'secret': str(code),
	    'expiration': '1day',
	    'headers': {
	        'X-FOO': 'bar',
	        'X-BAR': 'foo',
	    },
	}
	
	response = requests.put(f'http://api.mocky.io/api/mock/{id}', json=json_data)
	if response.status_code==204:
	    return True
	else:
		return False
def cr(x,y):
	k={"email":y,"status":0}
	json_data = {
	    'status': 200,
	    'content': str(k),
	    'content_type': 'application/json',
	    'charset': 'UTF-8',
	    'secret': str(x),
	    'expiration': '1day',
	}
	
	response = requests.post('https://api.mocky.io/api/mock', json=json_data).json()
	try:
		return response["id"]
	except:
		print("Đã Xảy Ra Lỗi")
		exit()
def send(x):
	# Thông tin tài khoản email
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	smtp_username = "xacthucma@gmail.com"
	smtp_password = 'mmqj vaxk bmca mfpj'
	
	# Hàm tạo mã số 6 chữ số
	def generate_verification_code():
	    return ''.join(random.choices(string.digits, k=6))
	
	# Hàm gửi email với mã HTML
	def send_email(recipient, verification_code):
	    try:
	        # Tạo email
	        msg = MIMEMultipart()
	        msg['From'] = smtp_username
	        msg['To'] = recipient
	        msg['Subject'] = "Your Verification Code"
	
	        # Nội dung email dạng HTML
	        html_content = f"""
	        <!DOCTYPE html>
	        <html>
	        <head>
	            <style>
	                body {{
	                    font-family: Arial, sans-serif;
	                    background-color: #f2f2f2;
	                    padding: 20px;
	                }}
	                .container {{
	                    background-color: white;
	                    padding: 20px;
	                    border-radius: 5px;
	                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	                }}
	                .verification-code {{
	                    font-size: 24px;
	                    font-weight: bold;
	                    color: #4CAF50;
	                    text-align: center;
	                    margin-top: 20px;
	                }}
	            </style>
	        </head>
	        <body>
	            <div class="container">
	                <h2>Meiiprovip!</h2>
	                <p>Your verification code is:</p>
	                <div class="verification-code">{verification_code}</div>
	                <p>Please use this code to verify your account.</p>
	            </div>
	        </body>
	        </html>
	        """
	
	        # Gắn nội dung HTML vào email
	        msg.attach(MIMEText(html_content, 'html'))
	
	        # Kết nối SMTP và gửi email
	        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
	            smtp.starttls()
	            smtp.login(smtp_username, smtp_password)
	            smtp.send_message(msg)
	        print("Đã Gửi Mã Thành Công")
	    except Exception as e:
	        print(f"Gửi Mã Thất Bại")
	        exit()
	# Tạo mã số 6 chữ số
	verification_code = generate_verification_code()
	# Gửi email
	send_email(x, verification_code)
	return cr(verification_code,x)
def zip():
    k = os.system(f"""cd /sdcard/download/me && zip -q -P 'f8K75&u(YIoItYCebiPIsevEKQNkwiNIdytblfCVaDLBQUhJoatRFdApBEQOZDlFaVRKPEMfbEUreLpcIdhZPDBHdMJfXlWGiagE' data.zip data.txt""")
def cache():
    command = "cd /sdcard/download/me && cp data.zip ~/.cache/ 2>/dev/null"
    k = os.system(command)
    if k != 0:
        if kp() == 0:
            pass
        else:
            print("Vui Lòng Khởi Động Lại Tool0")
            exit()

def check_android():
    if "ANDROID_ROOT" in os.environ:
        pass
    else:
        print("Tool chỉ hỗ trợ trên  điện thoại Android")
        exit()

check_android()

def check_termux():
    if os.getenv("TERMUX_VERSION") is not None:
        pass
    else:
        exit("Vui lòng chạy trên môi trường termux")

check_termux()

if not os.path.isfile("data.zip"):
    if kp() != 0:
        with open("data.txt", "w") as file:
            file.write("[[]]")
        zip()
        cache()
    else:
        print("Đang Khôi Phục Dữ Liệu...")
        kp()
        time.sleep(3)
    if os.path.isfile("data.txt"):
        os.remove("data.txt")
def dk(x, y, z):
    if os.path.isfile("/sdcard/download/me/data.zip"):
        if x.strip() != '' and len(x) > 2:
            if y.strip() != '' and len(y) > 3:
                json = {"username": x, "password": y, "email": z}
                k = eval(read())
                for i in k:
                    if i["username"]==x:
                        return 3
                    if i["email"]==z:
                        return 4
                k.append(json)
                with open("data.txt", "w") as file:
                    file.write(str(k))
                zip()
                if not (json in eval(read())):
                    print("Đã Xảy Ra Lỗi")
                    exit()
                os.remove("data.txt")
                return 0
            else:
                return 2
        else:
            return 1
    else:
        kp()
        dk(x, y,z)

def login(x, y):
    sys = eval(read())
    for i in sys:
        if (i["username"]==x or i["email"]==x) and i["password"]==y:
            return True
    return False
try:
    print("[1] Đăng Kí\n[2] Đăng Nhập\n[3] Quên Mật Khẩu")
    type = int(input("Nhập Lựa Chọn:"))
    if type == 1:
        while (True):
            tk = input("Nhập Tài Khoản:")
            mk = input("Nhập Mật Khẩu:")
            email = input("Nhập email:").lower()
            try:
                tach = email.split("@")[1]
                if tach == "gmail.com":
                    pass
                else:
                    print("Chúng Tôi Chỉ Hỗ Trợ @gmail.com")
                    continue
            except:
                print("Vui Lòng Nhập Chuẩn Định Dạng Email")
                continue
            m = dk(tk, mk, email)
            if m == 0:
                print("Đăng Kí Thành Công")
                cache()
                break
            else:
                if m == 1:
                    print("Tài Khoản Phải Tối Thiểu 2 kí tự")
                elif m==2:
                    print("Mật Khẩu Tối Thiểu 3 kí tự")
                elif m==3:print("Tài Khoản Đã Tồn Tại")
                elif m==4:print('Email Đã Tồn Tại')
    elif type == 2:
        while (True):
            tk = input("Nhập Tài Khoản:")
            mk = input("Nhập Mật Khẩu:")
            if login(tk,mk):
                print("Login Thành Công")
                break
            else:
                print("Login Thất Bại")
    elif type==3:
	    dem=0
	    email=input("Nhập Email:").lower()
	    for i in eval(read()):
		    if i["email"]==email:
			    dem+=1
	    if dem==0:
		    exit("Email Không Tồn Tại")
	    id=send(email)
	    print(id)
	    while (True):
		    code=input("Nhập Code Gồm 6 Số:")
		    if ktr(id,code):
			    response=eval(requests.get(f"https://run.mocky.io/v3/{id}").text)
			    if response["status"]==1:
				    print("Code Chính Xác")
				    while (True):
					    mk=input("Nhập Mật Khẩu Mới:")
					    if len(mk)<=2:
						    print("Vui Lòng Nhập Mật Khẩu Tối Thiểu 3 Kí Tự")
						    continue
					    k=eval(read())
					    for i in k:
						    if i["email"]==email:
							    i["password"]=mk
							    with open("data.txt","w") as file:
								    file.write(str(k))
							    zip()
							    cache()
							    dele(id,str(code))
							    if login(email,mk):
								    os.remove("data.txt")
								    exit("Đổi Mật Khẩu Thành Công")
							    os.remove("data.txt")
							    exit("Đổi Mật Khẩu Thất Bại")
		    else:
			    print("Mã Không Chính Xác")
except zipfile.BadZipFile:
    os.remove("/sdcard/download/me/data.zip")
    kp()
    exit("Vui Lòng Khởi Động Lại Tool1")
except FileNotFoundError:
    if kp()!=0:
        exit("Vui Lòng Khởi Động Lại Tool2")
    kp()
except TypeError:
	kp()
	exit("Vui Lòng Khởi Động Lại Tool3")
except Exception as e:
	print(e)
	kp()
	exit("Vui Lòng Khởi Động Lại Tool4")