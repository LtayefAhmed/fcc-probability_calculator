import copy
import random

class Hat:
    def __init__(self,**color_counts):
        if len(color_counts) < 1:
            raise TypeError("you should at least put a color")
        self.contents=[]
        for color,count in color_counts.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self,num_balls):
        if num_balls >= len(self.contents):
            all_balls=self.contents.copy()
            self.contents.clear()
            return all_balls
        balls_drawn=[]
        for _ in range(num_balls):
            random_index=random.randint(0,len(self.contents)-1)
            ball_drawn=self.contents.pop(random_index)
            balls_drawn.append(ball_drawn)
        return balls_drawn




def experiment(hat, expected_balls,num_balls_drawn, num_experiments):
    
    success_count=0
    for _ in range(num_experiments):
        #copy
        hat_copy=copy.deepcopy(hat)
        #draw balls
        balls_drawn=hat_copy.draw(num_balls_drawn)
        
        # we put the balls in a dict to then compare
        balls_drawn_dict={}
        for color in balls_drawn:
        #here when the color first appear it sets the count to 1
            if color in balls_drawn_dict:
                balls_drawn_dict[color]+=1
            else:
                balls_drawn_dict[color]=1
        #compare with the expected balls
        success=True
        for required_color,required_count in expected_balls.items():
            #get returns 0 if the color doesn't exist
            actual_count=balls_drawn_dict.get(required_color,0)
            #if the actual count is less than the required count
            if actual_count < required_count:
                success=False
                break
        if success:
            success_count+=1
    return success_count / num_experiments

    


print(experiment(Hat(blue=4,red=2,green=6),{"blue":2,"green":1},3,1000))
        
        
