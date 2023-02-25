quiz = {
    "question 1":{
        "question" : "What is the capital of france ?",
        "answer": "Paris"
    },
    "question 2":{
        "question" : "What is the capital of Spain ?",
        "answer": "Madrid"
    },
    "question 3":{
        "question" : "What is the capital of Germany ?",
        "answer": "Berlin"
    },
    "question 4":{
        "question" : "What is the capital of Italy ?",
        "answer": "Rome"
    },
    "question 5":{
        "question" : "What is the capital of Austria ?",
        "answer": "Vienna"
    }
}


score =0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer ?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score+=1
        print("your score is :", score)
    else:
        print('Wrong')
        print("Your score is :"+str(score))
