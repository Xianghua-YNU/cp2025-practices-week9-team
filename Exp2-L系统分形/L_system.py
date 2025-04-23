"""
项目2: L-System分形生成与绘图模板
请补全下方函数，实现L-System字符串生成与绘图。
"""
import matplotlib.pyplot as plt
import math

def apply_rules(axiom, rules, iterations):
    """
    生成L-System字符串
    :param axiom: 初始字符串（如"F"或"0"）
    :param rules: 规则字典，如{"F": "F+F--F+F"} 或 {"1": "11", "0": "1[0]0"}
    :param iterations: 迭代次数
    :return: 经过多轮迭代后的最终字符串
    """
    # TODO: 实现L-System字符串生成逻辑
    current=axiom
    for _ in range(iterations):
        next_str = []
        for char in current:
            next_str.append(rules.get(char,char))
        current=' '.join(next_str)
    return current

def draw_l_system(instructions, angle, step, start_pos=(0,0), start_angle=0, savefile=None,tree_mode=False,title=()):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串（如"F+F--F+F"）
    :param angle: 每次转向的角度（度）
    :param step: 每步前进的长度
    :param start_pos: 起始坐标 (x, y)
    :param start_angle: 起始角度（0表示向右，90表示向上）
    :param savefile: 若指定则保存为图片文件，否则直接显示
    """
    # TODO: 实现L-System绘图逻辑
    x,y=start_pos
    current_angle=start_angle
    stack=[]
    fig, ax = plt.subplots()

    for cmd in instructions:
        if cmd in ('F','0','1'):
            new_x=x+step*math.cos(math.radians(current_angle))
            new_y=y+step*math.sin(math.radians(current_angle))
            ax.plot([x,new_x],[y,new_y],'b-' if tree_mode else 'green',linewidth=1.2 if tree_mode else 1)
            x,y=(new_x,new_y)
        elif cmd == '+':
            current_angle+=angle
        elif cmd == '-':
            current_angle-=angle
        elif cmd == '[':
            stack.append((x,y,current_angle))
            if tree_mode:
                current_angle+=angle
        elif cmd == ']':
            x,y,current_angle=stack.pop()
            if tree_mode:
                current_angle-=angle
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title(title)
    if savefile:
        plt.savefig(savefile, bbox_inches='tight',pad_inches=0.1,dpi=150)
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    """
    主程序示例：分别生成并绘制科赫曲线和分形二叉树
    学生可根据下方示例，调整参数体验不同分形效果
    """
    # 1. 生成并绘制科赫曲线
    #生成并绘制科赫曲线
    koch_axiom="F"   #公理
    koch_rules={"F":"F+F--F+F"}   #规则
    koch_iterations=4   #迭代次数
    koch_angle=60   #转角
    koch_step=5   #步长
    koch_instr=apply_rules(koch_axiom,koch_rules,koch_iterations)#生成指令字符串
    #plt.figure(figsize=(10,3))
    draw_l_system(koch_instr,koch_angle,koch_step,title="L-System Koch Curve")   #绘图并保存
    plt.show()

    # 2. 生成并绘制分形二叉树
    axiom="0"
    rules={"1":"11","0":"1[0]0"}
    iterations=7
    angle=45
    step=7
    instr=apply_rules(axiom,rules,iterations)
    #plt.figure(figsize=(7,7))
    draw_l_system(instr,angle,step,start_angle=90,tree_mode=True,title="L-System Fractal Tree")
    plt.show()
