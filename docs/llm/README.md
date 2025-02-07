# llm

## Description
Get information on a specific LLM or list all information for all supported LLMs.

## Synopsis

```
[-m MODEL_ID]
```

## Options
> Not passing `-m` flag will list all information for all supported LLMs

`-m MODEL_ID`
> Show information on the model with id MODEL_ID

## Examples
`$ york-genai-calc llm -m ai21.jamba-1.5-large`

**Response**
```
{
    "models": [
        {
           "provider_id":"ai21",
           "provider_name_pretty":"AI21",
           "model_id":"ai21.jamba-1.5-large",
           "model_name_pretty":"Jamba 1.5 Large",
           "cost_per_1k_input_tokens":0.002,
           "cost_per_1k_output_tokens":0.008
        }
    ]
}
```

`$ york-genai-calc llm`

**Response**
```
{
   "models":[
      {
         "provider_id":"ai21",
         "provider_name_pretty":"AI21",
         "model_id":"ai21.jamba-1.5-large",
         "model_name_pretty":"Jamba 1.5 Large",
         "cost_per_1k_input_tokens":0.002,
         "cost_per_1k_output_tokens":0.008
      },
      {
         "provider_id":"ai21",
         "provider_name_pretty":"AI21",
         "model_id":"ai21.jamba-1.5-large.bedrock",
         "model_name_pretty":"Jamba 1.5 Large (AWS Bedrock)",
         "cost_per_1k_input_tokens":0.002,
         "cost_per_1k_output_tokens":0.008
      },
      {
         "provider_id":"ai21",
         "provider_name_pretty":"AI21",
         "model_id":"ai21.jamba-1.5-mini",
         "model_name_pretty":"Jamba 1.5 Mini",
         "cost_per_1k_input_tokens":0.0002,
         "cost_per_1k_output_tokens":0.0004
      },
      ...
   ]
}
```
