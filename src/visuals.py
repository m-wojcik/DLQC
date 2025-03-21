import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import numpy as np

from matplotlib.pyplot import Figure

def plotBlochSphere():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set(xlim3d=[-1.2,1.2], ylim3d=[-1.2,1.2], zlim3d=[-1.2,1.2])
    npoints = 100

    r = 1
    u = np.linspace(0,2*np.pi, npoints)
    v = np.linspace(0, np.pi, npoints)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x,y,z, color='linen', alpha=0.4)

    theta = np.linspace(0, 2*np.pi, npoints)
    straight = np.zeros(npoints)
    round1 = r * np.sin(theta)
    round2 = r * np.cos(theta)

    ax.plot(round1, round2, straight, color='black', alpha=0.75)
    ax.plot(straight, round1, round2, color='black', alpha=0.75)
    #ax.plot(round1, straight, round2, color='black', alpha=0.75)

    line = np.linspace(-r,r,npoints)

    ax.plot(line, straight, straight, color='black', alpha=0.6)
    ax.plot(straight, line, straight, color='black', alpha=0.6)
    ax.plot(straight, straight, line, color='black', alpha=0.6)
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))

    return fig, ax

def plotBlochSphereTrajectory(trajx, trajy, trajz, nframes, title='bloch.mp4', writer='ffmpeg'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set(xlim3d=[-1.2,1.2], ylim3d=[-1.2,1.2], zlim3d=[-1.2,1.2])
    npoints = 100

    r = 1
    u = np.linspace(0,2*np.pi, npoints)
    v = np.linspace(0, np.pi, npoints)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x,y,z, color='linen', alpha=0.4)

    theta = np.linspace(0, 2*np.pi, npoints)
    straight = np.zeros(npoints)
    round1 = r * np.sin(theta)
    round2 = r * np.cos(theta)

    ax.plot(round1, round2, straight, color='black', alpha=0.75)
    ax.plot(straight, round1, round2, color='black', alpha=0.75)
    #ax.plot(round1, straight, round2, color='black', alpha=0.75)

    line = np.linspace(-r,r,npoints)

    ax.plot(line, straight, straight, color='black', alpha=0.6)
    ax.plot(straight, line, straight, color='black', alpha=0.6)
    ax.plot(straight, straight, line, color='black', alpha=0.6)
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))

    
    
    #line = ax.plot(trajx[:1], trajy[:1], trajz[:1])[0]
    
    def update(frame, line):
        #ar.remove()
        #ar = ax.quiver(0, 0, 0, # <-- starting point of vector
        #    trajx[frame], trajy[frame], trajz[frame], # <-- directions of vector
        #    color = 'magenta', alpha = 1, lw = 3,
        #    arrow_length_ratio = 0.15)
        
        line_data = np.array([trajx[:frame], trajy[:frame], trajz[:frame]])
        line.set_data_3d(line_data)
        #print(line_data)
        #print()
        #bs = np.linspace(0,1,frame) / nframes
        #cols = np.array([1,1,bs[k]] for k in range(frame))
        #line.set_color(cols)
        
        return (line,)
    
    line = ax.plot([], [], [])[0]
    #ar = ax.quiver(0, 0, 0, # <-- starting point of vector
    #        trajx[0], trajy[0], trajz[0], # <-- directions of vector
    #        color = 'magenta', alpha = 1, lw = 3,
    #        arrow_length_ratio = 0.15)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ani = animation.FuncAnimation(fig=fig, func=update, fargs=(line,), frames=nframes, interval=30)
    ani.save(filename=title, writer=writer)


