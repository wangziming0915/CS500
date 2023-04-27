class Month:
    mapping = {"January": 0, "February": 1, "March":2, "April":3, "May":4, "June":5, "July":6, "August":7, "September":8, "October":9, "November":10, "December":11}
    mapping2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    def __init__(self, month_name: str) -> None:
        self.month_number = self.mapping[month_name]

    def advance(self) -> None:
        self.month_number += 1
    
    def prev(self) -> None:
        self.month_number -= 1

    def display(self) -> None:
        print(self.mapping2[self.month_number])

    def compare(self, m: "Month") -> int:
        if self.month_number > m.month_number:
            return 1
        elif self.month_number < m.month_number:
            return -1
        else:
            return 0

def main():
    month1 = Month("January")
    month2 = Month("February")
    month1.advance()
    month2.prev()
    month1.display()
    print(month1.compare(month2))
    print(month1.month_number)
    print(month2.month_number)

    
if __name__ == "__main__":
    main()
