"""websocket"""

# WebSocket 是 HTML5 开始提供的一种在单个 TCP 连接上进行全双工通讯的协议
import asyncio
import websockets


async def listen():
    uri = "wss://example.com/socket"  # 替换为你要连接的 WebSocket 服务器的 URL
    # 通过 websockets.connect 连接到 WebSocket 服务器
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        try:
            # 使用 while True 循环不断接收消息，并将接收到的消息打印到控制台
            while True:
                message = await websocket.recv()
                print(f"Received message: {message}")
        # 捕获 websockets.ConnectionClosed 异常，处理连接关闭的情况
        except websockets.ConnectionClosed:
            print("Connection closed")


if __name__ == "__main__":
    asyncio.run(listen())
