import httpx
from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup

mcp = FastMCP(
    'your MCP tools',
    dependencies=['beautifulsoup4']
)

@mcp.tool(
    name='extract-web-page-content-tool',
    description='Tool to extract page content in text format'
)

def extract_web_content(url:str)->str|None:
    """
    Extract text content from a web page.
    Args:
        url: URL of the web page to extract content from.

    Returns:
        str:Extracted text content from the web page.
    """
    try:
        response = httpx.get(
            url,
            headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'
            },
            timeout=10.0,
            follow_redirects = True
        )
        response.raise_for_status()
        soup=BeautifulSoup(response.text,'html.parser')
        return soup.get_text().replace('\n',' ').replace('\r',' ').strip()
    except Exception as e:
        return f'Error fetching content:{str(e)}'

if __name__=="__main__":
    mcp.run(transport='stdio')