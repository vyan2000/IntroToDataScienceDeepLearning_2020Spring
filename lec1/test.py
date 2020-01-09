#########################################################################
### Introduction to Software Engineering, Data Science, and Deep Learning
### Shenzhen University
### Computer Vision and Machine Learning Research Group
### Instructor: Yan Yan
### Email: yyan@szu.edu.cn
### Lec 1: basic software development techniques
#########################################################################

def hello():
    print("hello world \n");
    
def add(a,b):
    c = a+b;
    return c 


def main():
    hello();
    a = 1; b = 2;
    c = add(a,b);
    print("c = a+b, c is ", c)

    

if __name__ == "__main__":
    main()
