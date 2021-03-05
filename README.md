# patent
A set of tools for extracting info from a google patent


### Installation
    pip install patent

### Recommended Usage
    import patent

    a_patent = patent.get('US20170081441A1')
    print(a_patent.title)
    for inventor in a_patent.inventors:
        print(inventor)
    
    for claim in a_patent.claims:
        if claim.parent_id:
            print(claim.text)
    
### Examples
