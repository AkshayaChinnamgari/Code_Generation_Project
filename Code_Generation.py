operator = ['+','-','*','/','@']
def operand(exp):
  r=exp[::-1]
  for j in range(len(r)):
    if r[j] not in operator:
       return j
def generate_assembly_code(exp):
    stack = []
    temp = 1
    assembly = ""
    operator = ['+','-','*','/','@']
    l = operand(exp)
    n=len(exp)
    for i in range(n):
        char = exp[i]
        if char.isalpha():
            stack.append(char)
        elif char == "@":
                op = stack.pop()
                if op != '$0':
                   assembly += f"L {op}\n"
                assembly += f"N\n"
                stack.append(f"${temp%2}")
                assembly += f"ST ${temp}\n"
                temp += 1
        elif ((exp[i-1]) in operator and (exp[i]) == '-'):
                op = stack.pop()
                if op != '$0':
                   assembly += f"L {op}\n"
                assembly += "N\n"
                assembly += f"A ${str(temp%2)}\n"
                stack.append("$" + str(temp%2))                
                temp += 1
        else:
            operand2 = stack.pop()
            if len(stack) != 0:
               operand1 = stack.pop()
            
            if(exp[i] in operator and exp[i-1] not in operator):
              if operand1 not in ['$0', '$1', '$2']:
                 assembly += f"L {operand1}\n"
              if char == '+':
                assembly += f"A {operand2}\n"
              elif char == '-':
                assembly += f"S {operand2}\n"
              elif char == '*':
                assembly += f"M {operand2}\n"
              elif char == '/':
                assembly += f"D {operand2}\n"

              if temp < 3:
                if(exp[i] in operator and exp[i-1] not in operator):
                  assembly += f"ST ${str(temp)}\n"
                  if i != (len(exp)-1):
                    if(exp[i+1]) == "+":
                       assembly += f"A ${str((temp%2)+1)}\n"
                    if(exp[i+1]) == "*":
                       assembly += f"M ${str((temp%2)+1)}\n"
                    if(exp[i+1]) == "/":
                       assembly += f"D ${str((temp%2)+1)}\n"
                
              else:
                if(exp[i] in operator and exp[i-1] not in operator):
                  if(exp[i+1]) == "+":
                    assembly += f"A ${str((temp%2)+1)}\n"
                  if(exp[i+1]) == "*":
                    assembly += f"M ${str((temp%2)+1)}\n"
                  if(exp[i+1]) == "/":
                    assembly += f"D ${str((temp%2)+1)}\n"
                
                if(i < n-l and exp[i] in operator and exp[i-1] not in operator):
                   assembly += f"ST ${str((temp%2)+1)}\n"

            stack.append("$" + str(temp%2))
            temp += 1      
    x = stack.pop()
    if x != '$0':
      if assembly[-2] != '1':
         if exp[-1] == '/':
            assembly += 'D ' + x
         elif exp[-1] == '*':
            assembly += 'M ' + x
         elif exp[-1] == '+':
            assembly += "A " + x
    return assembly
print(generate_assembly_code("AB+CD+EF++GH+++"))
