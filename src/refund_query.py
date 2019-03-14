from . import app, inspect

@app.app.route('/micro-pay/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def micro_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/jsapi/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def jsapi_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/native/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def native_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/app/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def app_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/h5/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def h5_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/micro-app/refund-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def micro_app_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')
