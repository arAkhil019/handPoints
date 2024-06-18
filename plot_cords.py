import matplotlib.pyplot as plt
import numpy as np

size = 1.3
def plotter(landmarks,angles):
    x = [landmark[0] for landmark in landmarks]
    y = [landmark[1] for landmark in landmarks]
    plt.scatter(x, y)
    for i, txt in enumerate(landmarks):
        plt.annotate(i, (x[i], y[i]))
        if i in angles:
            plt.annotate(int(angles[i]), (x[i], y[i]+0.01), color='red')
    plt.xlim(0, 1)
    plt.ylim(0, 1.3)
    plt.gca().invert_yaxis()
    plt.show()

#a plot of z values to know vairation in it
def plot_z(landmarks):
    z = [landmark[2] for landmark in landmarks]
    for i in range(0,21):
        plt.scatter(i,landmarks[i][2])
        plt.annotate(i, (i, landmarks[i][2]))
    x = np.arange(0,len(landmarks))
    plt.plot(x,z)
    plt.show()

lm = [(0.3173746168613434, 0.6556531190872192, 2.6269316322213854e-07), (0.3573490381240845, 0.7391464710235596, -0.02871072106063366), (0.42291656136512756, 0.780962347984314, -0.03877570480108261), (0.47646602988243103, 0.8086646199226379, -0.04664655774831772), (0.5173134207725525, 0.8359014391899109, -0.0556475892663002), (0.47981175780296326, 0.6748625636100769, -0.03540261462330818), (0.5472043752670288, 0.672366738319397, -0.05287661775946617), (0.5870393514633179, 0.6731800436973572, -0.0648273229598999), (0.6211641430854797, 0.672661304473877, -0.07551117986440659), (0.4773133397102356, 0.6076581478118896, -0.03851589560508728), (0.5487337112426758, 0.5725712180137634, -0.056464824825525284), (0.5949556827545166, 0.5544086694717407, -0.07207998633384705), (0.6329609155654907, 0.5362300276756287, -0.08532847464084625), (0.4564448595046997, 0.5531825423240662, -0.044724240899086), (0.5217974781990051, 0.4946240186691284, -0.06825275719165802), (0.5659174919128418, 0.4571504592895508, -0.08829569071531296), (0.6022416353225708, 0.42593926191329956, -0.10350503027439117), (0.4218538999557495, 0.5115479230880737, -0.05301246419548988), (0.457722544670105, 0.4252178966999054, -0.08107742667198181), (0.4840576648712158, 0.36982277035713196, -0.09924118220806122), (0.5094873309135437, 0.3251419961452484, -0.111921027302742)]
# plot_z(lm)
landmarks = [(0.3918011486530304, 0.8184689879417419, 3.885636488121236e-07), (0.43526801466941833, 0.7857915163040161, -0.03076496161520481), (0.45651715993881226, 0.6857698559761047, -0.03671840578317642), (0.4408324360847473, 0.5911962389945984, -0.04046129062771797), (0.41809380054473877, 0.5208394527435303, -0.04346301034092903), (0.48219630122184753, 0.59078449010849, 0.0019855813588947058), (0.5012534856796265, 0.4927218556404114, 0.0026841775979846716), (0.5142167806625366, 0.4257718324661255, 0.0007124877301976085), (0.5238659381866455, 0.3737376928329468, -0.003195668337866664), (0.4497750401496887, 0.5750798583030701, 0.005244034808129072), (0.45917779207229614, 0.45588600635528564, 0.005241789855062962), (0.4671698808670044, 0.38452088832855225, -0.003012394765391946), (0.47044461965560913, 0.32182714343070984, -0.009596739895641804), (0.416007936000824, 0.5849811434745789, 0.003197520039975643), (0.413338303565979, 0.492110013961792, -0.0209416002035141), (0.41243505477905273, 0.5345792770385742, -0.042369186878204346), (0.4092143774032593, 0.5660463571548462, -0.05050204321742058), (0.3854701817035675, 0.6119505167007446, -0.0005653455154970288), (0.38772881031036377, 0.5572518706321716, -0.03152942284941673), (0.38970085978507996, 0.6041803956031799, -0.04854777455329895), (0.39083608984947205, 0.6491822004318237, -0.056185800582170486)]
# plotter(landmarks)