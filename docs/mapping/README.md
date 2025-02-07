# mapping

## Description
Show the mapping between unique identifiers and display (pretty) names for either models or providers.

## Synopsis

```
{-p|-m}
```

## Options

`-p`  
> Show provider mapping  

**Response**
```
{
    "mapping": {
        "provider_id": "string",
        ...
    }
    
}
```

`-m`  
> Show model mapping

**Response**
```
{
    "mapping": {
        "model_id": "string",
        ...
    }
    
}
```
## Examples

`$ york-genai-calc mapping -p`

**Response**
```
{
   "mapping":{
      "ai21":"AI21",
      "amazon":"Amazon",
      "anthropic":"Anthropic",
      "cohere":"Cohere",
      "meta":"Meta",
      "mistral":"Mistral AI",
      "openai":"OpenAI"
   }
}
```