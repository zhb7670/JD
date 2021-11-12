// 编译对比
    contrastForm() {
      const params1 = this.originParams; // 未修改的数据
      const params2 = JSON.parse(JSON.stringify(this.form.params)); // 已修改的数据
      const res = [];
      Object.keys(params2).forEach((key) => {
        if (params1[key] !== params2[key]) {
          if (this.labelObj[key]) {
            // 如果是需要保存修改记录的字段, 才保存
            res.push({
              updateInfo: this.labelObj[key],
              before: params1[key],
              after: params2[key],
            });
          }
        }
      });
      return res;
    },