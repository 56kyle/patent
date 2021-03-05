
import patent


if __name__ == '__main__':
    google_patent = patent.get('CN1045110B', 'en')
    print(google_patent.title)
    print(google_patent.number)
    print(google_patent.inventors)
    print(google_patent.language)
    print(google_patent.claims)


