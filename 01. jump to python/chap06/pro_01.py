learn = open('learning_python.txt','r')
read_learn = learn.read()
c_learn = read_learn.replace("python", 'C')
learn.close()
add_learn = open('learning_python_copyed', 'a')
add_learn.write(read_learn)
add_learn.write(('\n'+c_learn))
add_learn.close()

