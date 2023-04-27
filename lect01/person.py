class Hand :
    def __init__(self):
        self._fingers = fingers

    @property
    def fingers(self):
        return self._fingers

    @fingers.setter
    def fingers(self, fingers):
        if fingers >= 0 and fingers <=  5:
            self._fingers = fingers
    
    def __str__(self) -> str:
        return 'Hand fingers = ' + str(self._fingers)


def main():
    f = Hand(5)
    print(f)

if __name__ == '__main__':
    main()