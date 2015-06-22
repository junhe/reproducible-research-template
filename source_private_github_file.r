# This function download my python downloader, and use the downloader to download
# the private file from github repository.
# Example:
# source_private_github_file("doraemon", "analysis/analyzer.r", "599060f45d97538b9dffda4b54ab88d1e7eff006")
source_private_github_file <- function(repo_name, file_path, commit)
{
    target_dir = "/tmp/dir_for_source_private_github_file_x32nd83sx"
    
    # download the downloader
    print("downloading the python downloader..")
    system('cd /tmp; curl -O https://gist.githubusercontent.com/junhe/806c57ce629e1d7035a1/raw/download_github_private_file.py')
    
    # execute the downloader
    print("downloading the private file using python downloader...")
    cmd = sprintf("source ~/.profile; python /tmp/download_github_private_file.py --repo_name %s --file_path %s --target_dir %s --commit %s",
        repo_name, file_path, target_dir, commit)
    system(cmd)

    basename = tail(unlist(strsplit(file_path, "/")), n=1)
    local_path = paste(target_dir, basename, sep="/")
    
    # sourcing the downloaded file
    print(paste("sourcing the downloaded file:", local_path))
    source(local_path)
}
