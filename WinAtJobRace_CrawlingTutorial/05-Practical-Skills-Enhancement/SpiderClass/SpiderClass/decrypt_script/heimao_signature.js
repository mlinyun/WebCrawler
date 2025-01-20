const crypto = require("crypto");

function get_search_url(kw, page) {
    // page 从 0 开始
    var p = new Date().getTime(),
        b = (function (e, t, r) {
            var n = "",
                i = t,
                a = [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                    "M",
                    "N",
                    "O",
                    "P",
                    "Q",
                    "R",
                    "S",
                    "T",
                    "U",
                    "V",
                    "W",
                    "X",
                    "Y",
                    "Z",
                ];
            e && (i = Math.round(Math.random() * (r - t)) + t);
            for (var o = 0; o < i; o++) {
                n += a[Math.round(Math.random() * (a.length - 1))];
            }
            return n;
        })(!1, 16),
        m = "$d6eb7ff91ee257475%";

    var u = kw,
        d = 10;
    var param = [p, b, "P0tk894Tcxi4t%S$"].sort().join("");

    var r = crypto.createHash("sha256").update(param).digest("hex");

    var url = ""
        .concat("//tousu.sina.com.cn/api/index/s", "?ts=")
        .concat(p, "&rs=")
        .concat(b, "&signature=")
        .concat(r);
    var ts = p,
        rs = b,
        signature = r;
    return ts + ";" + rs + ";" + signature;
}
