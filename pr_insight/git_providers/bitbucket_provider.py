from .git_provider import GitProvider, MAX_FILES_ALLOWED_FULL


def _gef_filename(diff):
    if diff.new.path:
        return diff.new.path
    return diff.old.path
        self.git_files = None
                          'publish_file_comments']:
        try:
            git_files = context.get("git_files", None)
            if git_files:
                return git_files
            self.git_files = [_gef_filename(diff) for diff in self.pr.diffstat()]
            context["git_files"] = self.git_files
            return self.git_files
        except Exception:
            if not self.git_files:
                self.git_files = [_gef_filename(diff) for diff in self.pr.diffstat()]
            return self.git_files

        try:
            pr_patches = self.pr.diff()
        except Exception as e:
            # Try different encodings if UTF-8 fails
            get_logger().warning(f"Failed to decode PR patch with utf-8, error: {e}")
            encodings_to_try = ['iso-8859-1', 'latin-1', 'ascii', 'utf-16']
            pr_patches = None
            for encoding in encodings_to_try:
                try:
                    pr_patches = self.pr.diff(encoding=encoding)
                    get_logger().info(f"Successfully decoded PR patch with encoding {encoding}")
                    break
                except UnicodeDecodeError:
                    continue

            if pr_patches is None:
                raise ValueError(f"Failed to decode PR patch with encodings {encodings_to_try}")

        diff_split = ["diff --git" + x for x in pr_patches.split("diff --git") if x.strip()]
                if diffs[i].data.get('lines_added', 0) == 0 and diffs[i].data.get('lines_removed', 0) == 0:
                    diff_split[i] = ""
                elif len(diff_split_lines) <= 3:
                    diff_split[i] = ""
                    get_logger().info(f"Disregarding empty diff for file {_gef_filename(diffs[i])}")
                else:
                    get_logger().warning(f"Bitbucket failed to get diff for file {_gef_filename(diffs[i])}")
                    diff_split[i] = ""
        counter_valid = 0
        # get full files
            file_path = _gef_filename(diff)
            if not is_valid_file(file_path):
                invalid_files_names.append(file_path)
                counter_valid += 1
                if get_settings().get("bitbucket_app.avoid_full_files", False):
                    new_file_content_str = ""
                elif counter_valid < MAX_FILES_ALLOWED_FULL // 2:  # factor 2 because bitbucket has limited API calls
                    if diff.old.get_data("links"):
                        original_file_content_str = self._get_pr_file_content(
                            diff.old.get_data("links")['self']['href'])
                    else:
                        original_file_content_str = ""
                    if diff.new.get_data("links"):
                        new_file_content_str = self._get_pr_file_content(diff.new.get_data("links")['self']['href'])
                    else:
                        new_file_content_str = ""
                    if counter_valid == MAX_FILES_ALLOWED_FULL // 2:
                        get_logger().info(
                            f"Bitbucket too many files in PR, will avoid loading full content for rest of files")
                    original_file_content_str = ""
                file_path,
    def create_inline_comment(self, body: str, relevant_file: str, relevant_line_in_file: str,
                              absolute_position: int = None):
                                                                                relevant_file.strip('`'),
                                                                                relevant_line_in_file,
                                                                                absolute_position)
    def publish_inline_comment(self, comment: str, from_line: int, file: str, original_suggestion=None):
        payload = json.dumps({
            elif 'start_line' in comment:  # multi-line comment
            elif 'line' in comment:  # single-line comment
        files = {file_path: contents}
        data = {
        headers = {'Authorization': self.headers['Authorization']} if 'Authorization' in self.headers else {}
        })