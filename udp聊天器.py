import socket

def sendto(udp):
	#输入的内容
	data=input('请输入您想输入的：')
	#请输入目标的ip地址和端口号
	ipaddress=input("输入目标ip:")
	netstat=int(input("输入目标端口:"))  # 因为input自动转化为str类型，所以要加int
	#发送数据
	udp.sendto=(data.encode('utf-8'),(ipaddress,netstat))

def recv(udp):
	#接收数据
	recv_data=udp.recvform(1024)
	#显示接收的数据
	print('%s:%s',str(recv_data[1]),recv_data[0].decode('gbk'))  # 与windows进行消息互通，转化成gbk

def main():
	#创套接层
	udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#进行绑定
	udp.bind(('',8080))
	# 创建循环
	
	while True:
		print("按1.进行发送数据")
		print("按2.进行接收数据")
		print("按3.退出程序")
		guess=int(input("请选择一下服务"))
		if guess==1:
			sendto(udp)
		elif guess==2:
			recv(udp)
		elif guess==3:
			break
		else:
			print("输入有误请重新输入")

if __name__ == '__main__':
	main()
