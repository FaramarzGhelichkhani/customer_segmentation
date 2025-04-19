import re
from openpyxl import load_workbook
from customer_segmentation.settings import BASE_DIR

PATH =  BASE_DIR.as_posix() + "/data/xlsxs/"

class FeatureExtractor:
    def __init__(self):
        # Define default replacements and abbreviations if none are provided
        self.replacements = self.load_data_from_excel(PATH  + "replacements.xlsx")
        self.abbreviations = self.load_data_from_excel(PATH + "abbreviations.xlsx")
        self.dict_car = self.load_data_from_excel(PATH + "cardinal_number_typo.xlsx")
        self.dict_ord = self.load_data_from_excel(PATH + "ordinal_number_typo.xlsx")
        self.keywords = ['طبقه', 'زنگ', 'واحد', 'بلوک', 'فاز', 'برج', 'کوچه','ساختمان','خیابان','منطقه','کد پستی','پلاک']
        self.irrelevant_keywords =[]
        # Predefined patterns for extracting plaque numbers
        self.plaque_pattern = re.compile(r'پلاک\s*(\d+)', re.IGNORECASE)
        self.floor_pattern = re.compile(r'طبقه\s*(\d+)', re.IGNORECASE)
        self.unit_pattern = re.compile(r'واحد\s*(\d+)', re.IGNORECASE)
        self.ordinal_pattern = self.compile_ordinal_pattern()
        self.cardinal_pattern = self.compile_cardinal_pattern()

    def load_data_from_excel(self, file_path):
        """Load a dictionary from a given Excel file."""
        wb = load_workbook(file_path)
        data_dict = {}
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            key, value = row
            # Ensure both key and value are strings, default value to empty string if None
            data_dict[str(key)] = str(value) if value is not None else ''
        return data_dict

    def compile_irrelevant_pattern(self):
        """Compile a regex pattern to remove irrelevant keywords and following numbers."""
        if self.irrelevant_keywords:
            keywords_pattern = '|'.join(f"({re.escape(keyword)})\s*\d+"  for keyword in self.irrelevant_keywords)
            # Pattern matches a keyword followed by any amount of whitespace and an optional number
            return re.compile(r'{}(?:\s+\d+)?'.format(keywords_pattern), re.IGNORECASE)
        return None

    def compile_ordinal_pattern(self):
            """Compile a regex pattern for abbreviations mapping."""
            if self.abbreviations:
                keys_pattern = '|'.join(re.escape(key) for key in self.dict_ord.keys())
                # Wrap the keys pattern in word boundaries
                return re.compile(r'\b({})\b'.format(keys_pattern), re.IGNORECASE)
            return None
    
    def compile_cardinal_pattern(self):
            """Compile a regex pattern for abbreviations mapping."""
            if self.abbreviations:
                keys_pattern = '|'.join(re.escape(key) for key in self.dict_car.keys())
                # Wrap the keys pattern in word boundaries
                return re.compile(r'\b({})\b'.format(keys_pattern), re.IGNORECASE)
            return None
        
    def clean_address(self, address, key):
        """Apply replacements, abbreviations, and remove irrelevant keywords."""

        # Apply replacements
        for char_to_replace, replacement_char in self.replacements.items():
            address = address.replace(char_to_replace, replacement_char)

        # Apply abbreviations
        for to_replace, replacement in self.abbreviations.items():
            address = re.sub(r'\b' + re.escape(to_replace) + r'\b', replacement, address)

        # Apply dict_ord
        address = self.ordinal_pattern.sub(lambda match: self.dict_ord[match.group(0)], address)
        
        # Apply dict_car
        address = self.cardinal_pattern.sub(lambda match: self.dict_car[match.group(0)], address)
  
        # Remove irrelevant parts based on specified key
        if key == 'plaque':
            self.irrelevant_keywords = list(set(self.keywords) - set(['پلاک']))
            irrelevant_pattern = self.compile_irrelevant_pattern()
            address = irrelevant_pattern.sub('', address)

        elif key == 'floor':
            self.irrelevant_keywords = list(set(self.keywords) - set(['طبقه']))
            irrelevant_pattern = self.compile_irrelevant_pattern()
            address = irrelevant_pattern.sub('', address)

        elif key == 'unit':
            self.irrelevant_keywords = list(set(self.keywords) - set(['واحد']))
            irrelevant_pattern = self.compile_irrelevant_pattern()
            address = irrelevant_pattern.sub('', address)    

        
        return address.strip()

    def extract_last_number(self, address):
        """Extract the last number from the address."""
        numbers = re.findall(r'\d+', address)
        return numbers[-1] if numbers else None

    def extract_plaque(self, address):
        """
        Extract plaque number from the given address, or return the last found number.

        Args:
            address (str): The address string from which to extract the plaque number.

        Returns:
            str or None: The extracted plaque number, or the last number found if no plaque is found.
        """
        cleaned_address = self.clean_address(address, 'plaque')
        # First attempt to match the plaque pattern
        match = self.plaque_pattern.search(cleaned_address)
        if match:
            return match.group(1)  # Return the numeric portion
        
        # If the plaque pattern is not found, return the last number in the address
        return self.extract_last_number(cleaned_address)

    def extract_floor(self, address):
            """
            Extract floor number from the given address, or return the last found number.

            Args:
                address (str): The address string from which to extract the floor number.

            Returns:
                str or None: The extracted floor number.
            """
            cleaned_address = self.clean_address(address, 'floor')
            # First attempt to match the plaque pattern
            match = self.floor_pattern.search(cleaned_address)
            if match:
                return match.group(1)  # Return the numeric portion
    
    def extract_unit(self, address):

            cleaned_address = self.clean_address(address, 'unit')
            # First attempt to match the plaque pattern
            match = self.unit_pattern.search(cleaned_address)
            if match:
                return match.group(1)  # Return the numeric portion
    