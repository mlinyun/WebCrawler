import hashlib


def get_verify_token(self, ts_10, params):
    # params 字符序列
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{k}={v}" for k, v in sorted_params])
    # 生成 token
    ts_md5 = hashlib.md5(f"{ts_10}{query_string}".encode()).hexdigest()
    return hashlib.md5(f"guaziclientuc{ts_md5}".encode()).hexdigest()

# 调用时候把自己的 header 和时间戳传入，就能拿到 token 值了
