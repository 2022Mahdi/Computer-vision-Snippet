#include <iostream>
#include <fstream>
#include <string>
#include <dirent.h>

int main() {
    std::string dir_path = "labels/";
    int total_lines = 0;
    DIR* dir = opendir(dir_path.c_str());
    struct dirent* entry;
    while ((entry = readdir(dir)) != NULL) {
        std::string filename = entry->d_name;
        std::string filepath = dir_path + "/" + filename;
        if (entry->d_type == DT_REG) {
            std::ifstream file(filepath);
            std::string line;
            while (std::getline(file, line)) {
                total_lines++;
            }
            file.close();
        }
    }
    closedir(dir);
    std::cout << "Total number of lines in all files: " << total_lines << std::endl;
    return 0;
}
