import re
def main():
    # First task: 166630675 
    with open('3/input', 'rt') as file:
        print(file) 
        pattern = re.compile(r"mul\(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\)")
        list = pattern.findall(file.read())
        first_task= 0
        for item in list:
            first_task+=int(item[0])*int(item[1])
        print(f"First task: {first_task}")
    with open('3/input', 'rt') as file:
        input = file.read()
        cleaned_content = re.sub(r'don\'t\(\)(.*?)(?=do\(\))', '', input, flags=re.DOTALL)
        pattern = re.compile(r"mul\(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\)")
        list = pattern.findall(cleaned_content)
        first_task= 0
        for item in list:
            first_task+=int(item[0])*int(item[1])
        print(f"Second task: {first_task}")
main()