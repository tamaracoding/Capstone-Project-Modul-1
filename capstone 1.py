from tabulate import tabulate

database = [{'id': 0,
             'species': 'cat',
             'breed': 'domestic short hair',
             'age': 0.5,
             'adoption_status': 'available',
             'sex': 'm',
             'special_care': 'none'},
             {'id': 1,
             'species': 'cat',
             'breed': 'havana brown',
             'age': 1,
             'adoption_status': 'adopted',
             'sex': 'f',
             'special_care': 'none'},
             {'id': 2,
             'species': 'dog',
             'breed': 'beagle mix',
             'age': 1.5,
             'adoption_status': 'available',
             'sex': 'f',
             'special_care': 'anticonvulsant'},
             {'id': 3,
             'species': 'dog',
             'breed': 'welsh corgi',
             'age': 2,
             'adoption_status': 'available',
             'sex': 'm',
             'special_care': 'hypoallergenic diet'}]

recycle_bin = []

# Fungsi untuk input angka
def input_numeric(prompt = 'enter number: '):
    user_input = input(prompt)
    try:
        # Try / mencoba konversi input menjadi float
        return float(user_input)
    except ValueError:
        # Jika konversi gagal, prompt lagi
        print('User input is not a valid number')
        return input_numeric(prompt)
# Fungsi untuk menambahkan data baru ke dalam database
def create_data():
    id = input_numeric("enter ID(ex:0 to 10): ")
    species = input("enter species: ")
    breed = input("enter breed: ")
    age = input_numeric("enter age in years: ") #bisa input float
    adoption_status = input("adopted/ available: ")
    sex = input("f (female) /m (male): ")
    special_care = input("special treatments needed: ")
    new_data = {'id': id,
             'species': species,
             'breed': breed,
             'age': age,
             'adoption_status': adoption_status,
             'sex': sex,
             'special_care': special_care}
    database.append(new_data)
# Fungsi untuk menampilkan data dalam bentuk tabel
def read_data(database):
    print(tabulate(database,
                   headers='keys',
                   tablefmt='psql'))
# Fungsi untuk mengupdate/mengubah data(kolom/row)
def update_data():
    row = int(input_numeric('row to update: '))
    column = input('column to update: ')
    if column in database[0].keys():
        if column == 'id':
            database[row][column] = input_numeric('enter id: ')
        elif column == 'species':
            database[row][column] = input('enter species: ')
        elif column == 'breed':
            database[row][column] = input('enter breed: ')
        elif column == 'age':
            database[row][column] = input_numeric('enter age in years: ')
        elif column == 'adoption_status':
            database[row][column] = input('adopted/available: ')
        elif column == 'sex':
            database[row][column] = input('enter sex: ')
        elif column == 'special_care': 
            database[row][column] = input('special treatments needed: ')
        else:
            print("the column you input is not available")
# Fungsi untuk menghapus data
def delete_data():
    row = int(input('row to delete: '))
    if row < 0 or row >= len(database):
        print("Invalid row number")
        return
    # Simpan data dalam recycle bin sebelum dihapus
    recycle_bin.append(database[row])
    del database[row]
# Fungsi untuk mengembalikan data yang sudah dihapus
def restore_data():
    row = int(input('row to restore from recycle bin: '))
    if row < 0 or row >= len(recycle_bin):
        print("Invalid row number")
        return
    database.append(recycle_bin[row])
    del recycle_bin[row]
def sort_id():
    sorted_id = sorted(database, key= lambda x: x['id'])
    print(tabulate(sorted_id, headers='keys', tablefmt='psql'))
# Fungsi untuk mengosongkan recycle bin
def empty_recycle_bin():
    del recycle_bin [:]
# Fungsi untuk melihat recycle bin
def view_recycle_bin():
    if recycle_bin:
        print(tabulate(recycle_bin, headers='keys', tablefmt='psql'))
    else:
        print("Recycle bin is empty")
# Fungsi untuk menyaring data berdasarkan spesies tertentu
def search_by_species():
    species = input('Enter species to search for: ')
    results = [entry for entry in database if entry['species'].lower() ==
               species.lower()]
    if results:
        print(tabulate(results, headers='keys', tablefmt='psql'))
    else:
        print(f"No entries found for species: {species}")
# Fungsi untuk menyaring data berdasarkan peranakan tertentu
def search_by_breeds():
    breed = input('Enter breeds to search for: ')
    results = [entry for entry in database if entry['breed'].lower() ==
              breed.lower()]
    if results:
        print(tabulate(results, headers='keys', tablefmt='psql'))
    else:
        print(f"No entries found for species: {breed}")
# Fungsi untuk menyaring data berdasarkan status adopsi
def search_by_adopt_stat():
    adopt_stat = input('Enter adoption status to check for: ')
    result = [entry for entry in database if entry['adoption_status'].lower() ==
              adopt_stat.lower()]
    if result:
        print(tabulate(result, headers='keys', tablefmt='psql'))
    else:
        print(f"No entries found for adoption_status: {adopt_stat}")
# Main Menu
def main():
    while True:
        print('''Welcome to "Pawsitive Vibes Shelter" Database Management System!
              Main Menu:
              1. Create Data of New Rescued Animals
              2. Read Current Database
              3. Update Database
              4. Delete Data in Database
              5. Restore Deleted Data
              6. Sort Database by ID in Ascending Order
              7. Empty Recycle Bin
              8. View Recycle Bin
              9. Search Database by Species
              10. Search Database by Breeds
              11. Search Database by Adoption Status
              12. Exit Main Menu''')
        user_input = input_numeric("Enter Menu (1 to 10): ")
        if user_input == 1:
            create_data()
        elif user_input == 2:
            read_data(database)
        elif user_input == 3:
            update_data()
        elif user_input == 4:
            delete_data()
        elif user_input == 5:
            restore_data()
        elif user_input == 6:
            sort_id()
        elif user_input == 7:
            empty_recycle_bin()
        elif user_input == 8:
            view_recycle_bin()
        elif user_input == 9:
            search_by_species()
        elif user_input == 10:
            search_by_breeds()
        elif user_input == 11:
            search_by_adopt_stat()
        elif user_input == 12:
            break
        else:
            print(f"Menu number {user_input} is not available")
main()