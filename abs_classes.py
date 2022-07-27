from abc import ABCMeta, abstractmethod
import shelve


class TemplateAbs(metaclass=ABCMeta):
    def __init__(self, filename) -> None:
        self.__filename = None
        self.filename = filename

    @abstractmethod
    def output():
        pass


class OutputAdressBook(TemplateAbs):
    def __init__(self, filename) -> None:
        super().__init__(filename)

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename):
        if filename is str:
            self.__filename = filename
        else:
            self.__filename = str(filename)

    def show__filename(self):
        return self.__filename

    def output(self):
        all_contacts_from_file = ''
        with shelve.open(self.__filename, flag='r') as states:
            for key in states:
                all_contacts_from_file += states[key].replace(
                    ',', ' ')+'\n'
            all_contacts_from_file = all_contacts_from_file[:-1].split('\n')
        print(all_contacts_from_file)


if __name__ == "__main__":
    a = OutputAdressBook('contacts')
    a.output()
