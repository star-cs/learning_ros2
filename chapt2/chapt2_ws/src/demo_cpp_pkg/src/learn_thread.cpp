#include <thread>
#include <iostream>
#include <chrono>
#include <functional>
#include "cpp-httplib/httplib.h"

using FuncBack = std::function<void(const std::string &, const std::string &)>;

class Download
{
public:
    void download(const std::string &host, const std::string &path, FuncBack callback)
    {
        std::cout << std::this_thread::get_id() << std::endl;
        httplib::Client cli(host);
        auto res = cli.Get(path);
        if (res && res->status == 200)
        {
            callback(path, res->body);
        }
    }

    void start_download(const std::string &host, const std::string &path, FuncBack callback)
    {
        std::thread(&Download::download, this, host, path, callback).detach();
    }
};

int main()
{
    auto d = Download();
    auto word_count = [](const std::string &path, const std::string &result) -> void
    {
        std::cout << "Downloaded " << path << " len " << result.length() << "--> " << result.substr(0, 9) << std::endl;
    };

    d.start_download("http://0.0.0.0:8000", "/novel1.txt", word_count);
    d.start_download("http://0.0.0.0:8000", "/novel2.txt", word_count);
    d.start_download("http://0.0.0.0:8000", "/novel3.txt", word_count);

    std::this_thread::sleep_for(std::chrono::seconds(10));
    return 0;
}