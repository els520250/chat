#讀取檔案
def read_file(filename):
	chat = []
	name = ''
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

#處理檔案
def process(filename):
	name = None
	chat = []
	for line in filename:
		if line == 'Allen' or line == 'Tom':
			name = line
			continue

		#name預設為空的，當name有值時才執行
		elif name:
			chat.append(name+ ': '+ line)
	return chat

#顯示輸出結果
def print_chat(chat):
	for line in chat:
		print(line)

#寫入檔案

def write_file(filename, chat):
	with open (filename, 'w', encoding='utf-8-sig') as f:
		for p in chat:
			f.write(p + '\n')


#主程式
def main():
	chat = read_file('input.txt')
	chat = process(chat)
	print_chat(chat)
	write_file('output.txt',chat)

main()