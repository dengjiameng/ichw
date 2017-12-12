# -*- coding: UTF-8 -*-
import json
from urllib.request import urlopen

#通过连接汇率服务，获取汇率结果。
#自定义字符串操作函数，对汇率参数进行校验，汇率结果进行二次处理。

	# 获取json字符串结果
	# url:汇率服务地址
def current_response(currency_from, currency_to, amount_from):
	try:
		url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
		response = urlopen(url)
		html = response.read()
		response.close()
		html = html.decode('ascii')
		return html
	except:
		return '404'


    # 测试current_response函数用例
    # 若连接汇率服务成功返回结果则测试通过
def test_current_response():
    assert (current_response('USD', 'EUR', 3.1) != '404')


	# 获取json字符串error信息
	# json_str:json格式字符串
def has_error(json_str):
    try:
        if type(json_str)==str:
            res = json.loads(json_str)
            return res['error']
        else:
            return json_str['error']
    except:
        return 'type case exception'


    # 测试has_error用例
    #若返回结果错误信息为空则测试通过
def test_has_error():
    result = current_response('USD', 'EUR', 3.1)
    assert (len(has_error(result)) == 0)


	# 校验参数是否为已存在的货币类型
	# param_currency：将要校验的货币代码
def is_currency(currency_from, currency_to, amount_from):
    result = current_response(currency_from, currency_to, amount_from)
    if '404' is result:
	    error_info = 'failed to connect to the exchange rate service';return error_info
    else:
        result_error = has_error(result);return result_error


    # 测试is_currency用例
    #若返回结果错误信息为空则测试通过
def test_is_currency():
    assert (is_currency('USD', 'EUR', 22.2) == '')


	# 获取响应货币查询时的值
	# json:汇率服务响应结果
def get_from(json_str):
    try:
        if type(json_str) == str:
            res = json.loads(json_str)
            return res['from']
        else:
            return json_str['from']
    except:
        return 'type case exception'


    # 测试get_from用例
    #若返回结果中from不为空则测试通过
def test_get_from():
    assert (get_from('{"from": "3.1 United States Dollars", "to": "2.5980945 Euros", "success": true, "error": ""}') != '')


	# 获取货币查询的响应值
	# json:汇率服务响应结果
def get_to(json_str):
    try:
        if type(json_str) == str:
            res = json.loads(json_str)
            return res['to']
        else:
            return json_str['to']
    except:
        return 'type case exception'


    # 测试get_to用例
    # 若返回结果中to不为空则测试通过
def test_get_to():
    assert (get_to('{"from": "3.1 United States Dollars", "to": "2.5980945 Euros", "success": true, "error": ""}') != '')


    #汇率转换，返回源货币金额值得目标货币类型的金额
	#currency_from:源货币类型
	#currency_to:目标货币类型
	#amount_from:货币金额
def exchange(currency_from, currency_to, amount_from):
    validate_result = is_currency(currency_from, currency_to, amount_from)
    if validate_result != '':
    	return validate_result
    result = current_response(currency_from, currency_to, amount_from)
    return get_to(result)


    #测试所有测试用例
def test_all():
    print("""test all cases""")
    test_current_response()
    test_has_error()
    test_is_currency()
    test_get_from()
    test_get_to()
    print('all tests passed')

# test_all()
print(exchange('USD', 'EUR', 20.1))

