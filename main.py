from quiz_engine import Quiz  # 필요한 모듈 및 함수들을 임포트
from question_bank import get_questions  # 필요한 모듈 및 함수들을 임포트
from utils import *  # 필요한 모듈 및 함수들을 임포트
from score_manager import save_result, plot_scores  # 필요한 모듈 및 함수들을 임포트

def main():  # 메인 함수 정의
    print("파이썬 퀴즈 게임에 오신 것을 환영합니다!")
    username = input("당신의 이름을 입력해주세요: ").strip()  # 사용자 이름 입력받기

    questions = get_questions()  # 퀴즈 문제 목록 불러오기
    quiz = Quiz(questions)  # Quiz 객체 생성
    question_number = 1

    while quiz.has_more_questions():  # 더 풀 문제가 있는 동안 반복
        question = quiz.get_next_question()  # 다음 문제 가져오기
        display_question(question, question_number)  # 문제와 선택지 화면에 출력
        user_choice = get_user_choice()  # 사용자로부터 선택지 입력받기
        correct = quiz.answer_question(question, user_choice)  # 정답 여부 판별

        if correct:
            print("정답입니다!")  # 정답 메시지 출력
        else:
            print(f"틀렸습니다! 정답은 '{question['options'][question['answer']]}' 입니다.")  # 오답 메시지와 정답 출력

        question_number += 1

    display_result(quiz.score, len(quiz.questions))  # 최종 점수 출력
    save_result(username, quiz.score)  # 사용자 이름과 점수 저장
    plot_scores()  # 점수 시각화 그래프 출력

    if quiz.incorrect_questions and ask_retry():  # 다시 도전할지 여부 확인
        retry_questions = quiz.incorrect_questions

        while retry_questions:
            print("\n틀린 문제 복습을 시작합니다.")
            retry_quiz = Quiz(retry_questions)  # Quiz 객체 생성
            question_number = 1
            retry_questions = []

            while retry_quiz.has_more_questions():
                question = retry_quiz.get_next_question()  # 다음 문제 가져오기
                display_question(question, question_number)  # 문제와 선택지 화면에 출력
                user_choice = get_user_choice()  # 사용자로부터 선택지 입력받기
                correct = retry_quiz.answer_question(question, user_choice)  # 정답 여부 판별

                if correct:
                    print("정답입니다!")  # 정답 메시지 출력
                else:
                    print(f"정답은 '{question['options'][question['answer']]}' 입니다.")
                    retry_questions.append(question)

                question_number += 1

            if retry_questions:
                print(f"\n{len(retry_questions)}문제를 다시 틀렸습니다. 다시 도전합니다.\n")
            else:
                print("\n모든 복습 문제를 맞혔습니다!")


if __name__ == "__main__":
    main()