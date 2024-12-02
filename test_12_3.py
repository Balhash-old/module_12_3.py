import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({place: str(runner) for place, runner in result.items()})

    @skip_if_frozen
    def test_start1(self):
        tourn = Tournament(90, self.runner1, self.runner3)
        results = tourn.start()
        self.all_results[1] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.runner3)

    @skip_if_frozen
    def test_start2(self):
        tourn = Tournament(90, self.runner2, self.runner3)
        results = tourn.start()
        self.all_results[2] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.runner3)

    @skip_if_frozen
    def test_start3(self):
        tourn = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tourn.start()
        self.all_results[3] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.runner3)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen  # Тест метода walk
    def test_walk(self):
        runner1 = Runner('Oleg')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @skip_if_frozen  # Тест метода run
    def test_run(self):
        runner = Runner('Alex')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner('Sergey')
        runner2 = Runner('Denis')
        for i in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance, )


if __name__ == '__main__':
    unittest.main()
