import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



def create_plots(name):
    with open(f"{name}.txt", "r") as data:
        params = []
        build = { i : [] for i in range(1,6) }
        trans = { i : [] for i in range(1,6) }
        solve = { i : [] for i in range(1,6) }
        lines = [ line[:-1] for line in data.readlines() ]
        idx = 0
        try:
            for i in range(1, 21):
                for j in range(1, 6):
                    line = lines[idx]
                    param = [ int(p) for p in line.split(" ") ]
                    params.append(param)
                    assert(param[0] == i and param[1] == j)
                    idx += 1
                    line = lines[idx]
                    build[param[1]].append(float(line.split(" ")[1]))
                    idx += 1
                    line = lines[idx]
                    trans[param[1]].append(float(line.split(" ")[1]))
                    idx += 1
                    line = lines[idx]
                    if line.startswith("Solving"):
                        solve[param[1]].append(float(line.split(" ")[1]))
                        idx += 1
                    else:
                        solve[param[1]].append(120.0)
        except:
            pass
    for i in range(1, 6):
        plt.plot(range(1,len(solve[i]) + 1), solve[i], label=f"{i} context" + ("s" if i > 1 else " "))
    plt.legend(loc='best')
    plt.xlabel("number of objects")
    plt.ylabel("runtime in seconds")
    plt.ylim(0,2)
    plt.xlim(1,20)
    plt.xticks([1, 5, 10, 15, 20])
    plt.savefig(f"{name}_solve.pdf")
    plt.cla() 
    plt.clf() 
    plt.close('all')

    for i in range(1, 6):
        plt.plot(range(1,len(trans[i]) + 1), trans[i], label=f"{i} context" + ("s" if i > 1 else " "))
    plt.legend(loc='best')
    plt.xlabel("number of objects")
    plt.ylabel("runtime in seconds")
    plt.ylim(0,2)
    plt.xlim(1,20)
    plt.xticks([1, 5, 10, 15, 20])
    plt.savefig(f"{name}_trans.pdf")
    plt.cla() 
    plt.clf() 
    plt.close('all')

    for i in range(1, 6):
        plt.plot(range(1,len(build[i]) + 1), build[i], label=f"{i} context" + ("s" if i > 1 else " "))
    plt.legend(loc='best')
    plt.xlabel("number of objects")
    plt.ylabel("runtime in seconds")
    plt.ylim(0,2)
    plt.xlim(1,20)
    plt.xticks([1, 5, 10, 15, 20])
    plt.savefig(f"{name}_build.pdf")
    plt.cla() 
    plt.clf() 
    plt.close('all')

create_plots("naive")
create_plots("specialized")