import matplotlib.pyplot as plt
from Algebra.EvFunctions import EvFunction as EvalFunc
from timeit import default_timer as timer
import numpy as np

if __name__ == "__main__":

    func = EvalFunc("x*sin(x**2)+x", 'x')
    func1 = EvalFunc("n**2", 'n')
    t = timer()
    x, y = func.evaluate(np.linspace(-5, 5, 3000))
    print(timer()-t)
    x1, y1 = func1.evaluate(np.linspace(-5, 5, 3000))
    k = func1.integrate__()
    n = func.diff__()
    n1 = k.diff__()
    print(k, n, n1)
    plt.tight_layout()
    plt.style.use('fivethirtyeight')
    plt.grid(True)
    plt.plot(x, y, '-g', label=str(func))
    plt.plot(x1, y1, '--b', label=str(func1))
    plt.xlabel("t_inv [ms]")
    plt.ylabel("u [V]")
    plt.legend()

    plt.show()

    """# func.displayFunction(grid=True, _yLabel="stepping Sine", _xLabel="time", color='g')
    # plt.savefig(fname="C:\\Users\\Dominik Lovetinsky\\Desktop\\MatlabExport_1.png", format='png')
    # with open("C:\\Users\\Dominik Lovetinsky\\Desktop\\MatlabExport_2.png", "wb") as exportTo:
    #     plt.savefig(fname=exportTo, format='png', dpi=1000)
    # plt.ion()
    data = pd.read_csv('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\data.csv')
    ids = data['Responder_id']
    language_response = data['LanguagesWorkedWith']
    print(type(data))
    languages = Counter()
    for i in language_response:
        languages.update(i.split(';'))

    usedLanguages = []
    peopleCount = []
    for item in languages.most_common(20):
        usedLanguages.append(item[0])
        peopleCount.append(item[1])

    usedLanguages.reverse()
    peopleCount.reverse()
    plt.tight_layout()
    plt.barh(usedLanguages, peopleCount, color='#ffa500')
    plt.xlabel('Number of people who use')
    plt.show()

    usedLanguages1 = []
    peopleCount1 = []
    for item in languages.most_common(5):
        usedLanguages1.append(item[0])
        peopleCount1.append(item[1])

    explode = [0.1, 0, 0, 0, 0]
    plt.pie(peopleCount1, labels=usedLanguages1, explode=explode,
            wedgeprops={'edgecolor': 'black'})
    plt.title('Most common programming languages')
    plt.show()
"""