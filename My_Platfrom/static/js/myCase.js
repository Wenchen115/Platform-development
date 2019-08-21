var ProjectInit = function (_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);
    var options = "";

    // 创建下拉列表
    function cmbAddOption(cmb, str) {
        console.log(str);
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        // option.obj = obj;

    }

    function getProjectListInfo() {
        // 获取某个用例信息
        $.get("project/get_project_list/", {}, function (resp) {
            if (resp.status == 10200) {
                console.log(resp.data);
                let dataList = resp.data;
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i], dataList[i]);
                }
                // cmbSelect(cmbProject, defaultProject);

            } else {
                window.alert(resp.message);
            }

        })

    }

    // 调用getProjectListInfo函数
    getProjectListInfo();

};