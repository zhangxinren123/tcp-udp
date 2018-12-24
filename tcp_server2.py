import	socket

def main():
	#1.创建套接字
	tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#2.绑定
	address=('',8080)
	tcp_server_socket.bind(address)
	#3.开启listen，将套接字属性变为被动
	tcp_server_socket.listen(128)
	while True:
		print('---------等待新的客户端---------')
		#4.使用accept拆分元祖,如果有新的客户端来链接服务器，则形成一个新套接字为这个客户端进行服务
		print('------------------------------')  # 方便显示
		new_tcp_server_socket,new_address=tcp_server_socket.accept()  # 所谓的accept其实就是等待客户端来connect
		print('++++++++++++++++++++++++++++++')  # 方便显示

		print(str(new_address)) #方便显示来访的主机地址
		while True:	
			#5.接收对方传来的数据
			recv_data=new_tcp_server_socket.recv(1024)
			
			print('客户端发送的数据是：%s'%recv_data.decode('utf-8'))

			#发送一些数据给对方
			new_tcp_server_socket.send('thank you,我已经接收'.encode('utf-8'))

		#6.关闭套接字
		new_tcp_server_socket.close()
	tcp_server_socket.close()

if __name__ == '__main__':
	main()