from . import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str

    class gpt_4:
        name: str = 'gpt-4'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Bing
        best_providers: list = [Provider.Bing, Provider.Lockchat]
        
    class palm:
        name: str = 'palm'
        base_provider: str = 'google'
        best_provider: Provider.Provider = Provider.Bard
        
            
    """    'falcon-40b': Model.falcon_40b,
    'falcon-7b': Model.falcon_7b,
    'llama-13b': Model.llama_13b,"""
    
    class falcon_40b:
        name: str = 'falcon-40b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
    
    class falcon_7b:
        name: str = 'falcon-7b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
        
    class llama_13b:
        name: str = 'llama-13b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
    
class ModelUtils:
    convert: dict = {
        'gpt-4': Model.gpt_4,
        
        'palm2': Model.palm,
        'palm': Model.palm,
        'google': Model.palm,
        'google-bard': Model.palm,
        'google-palm': Model.palm,
        'bard': Model.palm,
        
        'falcon-40b': Model.falcon_40b,
        'falcon-7b': Model.falcon_7b,
        'llama-13b': Model.llama_13b,
    }