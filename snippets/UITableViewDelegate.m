#pragma mark TableView Delegate/DataSource

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView{
    return <#number of section in table view#>;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
    return <#number of rows in section of a table view#>;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath{
    static NSString *cellIdentifier = <#the table view cell reuse identifire#>;
    <#UITableViewCellClass#> *cell = [tableView dequeueReusableCellWithIdentifier:cellIdentifier];
    
    //Make cell additional configuration here
    
    return cell;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath{
    //Handle the cell selection event here
}