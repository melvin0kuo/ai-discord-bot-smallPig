import sympy
async def calculate_math(message_to_edit, message, expression):
    try:
        # 将文字表达式转换为 sympy 表达式对象
        sympy_expr = sympy.sympify(expression)# 计算表达式的值
        result = sympy.N(sympy_expr)
        print(f'sympy:{result}')
        return f'sympy result:{result}'
    except sympy.SympifyError as e:
        return "無法計算: {str(e)}"
    except Exception as e:
        return "計算錯誤: {str(e)}"