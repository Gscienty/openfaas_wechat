import app, app_inspect

@app.app.route('/jsapi/unified-order', methods=[ 'POST' ])
@app_inspect.fields({ ('openid', 'sub_openid'), 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type' })
def jsapi_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')

@app.app.route('/native/unified-order', methods=[ 'POST' ])
@app_inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type' })
def native_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')

@app.app.route('/app/unified-order', methods=[ 'POST' ])
@app_inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type' })
def app_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')

@app.app.route('/h5/unified-order', methods=[ 'POST' ])
@app_inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type', 'scene_info' })
def h5_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')

@app.app.route('/micro-app/unified-order', methods=[ 'POST' ])
@app_inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type' })
def micro_app_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')
