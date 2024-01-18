import gym
from gym import spaces
import pygame , random , sys
import numpy as np

class math_game(gym.Env):

    def __init__(self):
        super(math_game, self).__init__()
        pygame.init()
        self.window_width, self.window_height = 800, 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("math.")
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 15)
        self.action_space = spaces.Discrete(11)  # 0 到 10 的整数，表示答案
        self.observation_space = spaces.Box(low=0, high=10, shape=(3,), dtype=int)
        self.reset()

    def reset(self):
        self.score = 0
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2
        return [self.num1, self.num2, self.score]

    def step(self, action): 
        self.user_answer = action
        done = False  # Initialize done
        if self.user_answer == self.correct_answer:
            reward = 10
        else:
            reward = -10
            # done = True

        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2
        self.score += reward
        return [self.num1, self.num2, self.score], reward, done, {}

    def render(self):
        # 在屏幕上显示游戏状态
        self.screen.fill(self.WHITE)
        question_text = self.font.render(f"{self.num1} + {self.num2} =", True, self.BLACK)
        self.screen.blit(question_text, (50, 50))
        score_text = self.font.render(f"score : {self.score}", True, self.BLACK)
        self.screen.blit(score_text, (50, 150))

        pygame.display.update()
        input_text = ""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_0, pygame.K_9 + 1):
                    input_text += event.unicode

    def run(self):
        self.render()
        action = int(input("ans : "))  # Cast input to int
        # print(self.step(action))
        return self.step(action)

    def close(self):
        pygame.quit()

if __name__ == "__main__":

    env = math_game()
    observation = env.reset()
    done = False

    while not done:
        env.run()