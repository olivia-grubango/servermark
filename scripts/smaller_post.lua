-- example HTTP POST script which demonstrates setting the
-- HTTP method, body, and adding a header

local body = io.open('data/smaller_tracks.json')
wrk.body = body:read("*all")
body.close()
wrk.method = "POST"
wrk.headers["Content-Type"] = "application/x-www-form-urlencoded"
