# Logger的继承（了解）
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S %p', )

ch = logging.StreamHandler()
ch.setFormatter(formatter)

logger1 = logging.getLogger('root')
logger2 = logging.getLogger('root.child1')
logger3 = logging.getLogger('root.child1.child2')

logger1.addHandler(ch)
logger2.addHandler(ch)
logger3.addHandler(ch)
logger1.setLevel(10)
logger2.setLevel(10)
logger3.setLevel(10)

logger1.debug('log1 debug')
logger2.debug('log2 debug')
logger3.debug('log3 debug')
